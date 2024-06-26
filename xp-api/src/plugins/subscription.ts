import fastifyPlugin from "fastify-plugin";
import { Subscription } from "../models/subscription.js";

export default fastifyPlugin(
  async (fastify) => {
    fastify.addHook("preHandler", async (request, reply) => {
      const subscriptionService = fastify.diContainer.resolve(
        "subscriptionService"
      );

      const user = request.user;

      if (!user) {
        return (request.subscription = null);
      }

      const subscription = await subscriptionService.getUserSubscription(
        user.id
      );

      request.subscription = subscription;
    });
  },
  {
    name: "payment",
    dependencies: ["auth", "di"],
  }
);

declare module "fastify" {
  export interface FastifyRequest {
    subscription: Subscription | null;
  }
}
