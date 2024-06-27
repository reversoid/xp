import fastifyPlugin from "fastify-plugin";
import { timingSafeEqual } from "node:crypto";
import { User } from "../models/user.js";

function timingSafeCompare(a: string, b: string) {
  const bufferA = Buffer.from(a);
  const bufferB = Buffer.from(b);

  const maxLength = Math.max(bufferA.length, bufferB.length);
  const paddedA = Buffer.concat([
    bufferA,
    Buffer.alloc(maxLength - bufferA.length),
  ]);
  const paddedB = Buffer.concat([
    bufferB,
    Buffer.alloc(maxLength - bufferB.length),
  ]);
  return timingSafeEqual(paddedA, paddedB);
}

export default fastifyPlugin(
  async (fastify) => {
    fastify.addHook("preHandler", async (request, reply) => {
      const apiKey = request.headers["api-key"];
      const tgUserId = request.headers["tg-user-id"];
      const userService = fastify.diContainer.resolve("userService");

      if (typeof apiKey !== "string") {
        request.user = null;
        return;
      }

      if (typeof tgUserId !== "string") {
        request.user = null;
        return;
      }

      if (!timingSafeCompare(fastify.config.API_KEY, apiKey)) {
        request.user = null;
        return;
      }

      const user = await userService.getUserByTgId(BigInt(tgUserId));

      request.user = user;
    });
  },
  {
    name: "auth",
    dependencies: ["env", "di"],
  }
);

declare module "fastify" {
  export interface FastifyRequest {
    user: User | null;
    paymentInfo: { firstPaidAt: Date; lastPaidAt: Date } | null;
  }
}
