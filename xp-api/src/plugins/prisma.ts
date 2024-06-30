import fp from "fastify-plugin";
import { PrismaClient } from "@prisma/client";
import { prismaClient } from "../db/prisma-client.js";

declare module "fastify" {
  interface FastifyInstance {
    prisma: PrismaClient;
  }
}

export default fp(
  async (fastify) => {
    await prismaClient.$connect();

    fastify.decorate("prisma", prismaClient);

    fastify.addHook("onClose", async (server) => {
      await server.prisma.$disconnect();
    });
  },
  { name: "prisma", dependencies: ["env"] }
);
