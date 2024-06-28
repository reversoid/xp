import fastifyPlugin from "fastify-plugin";

export default fastifyPlugin(
  async (fastify) => {
    fastify.addHook("preHandler", async (request, reply) => {
      const subscriptionService = fastify.diContainer.resolve(
        "subscriptionService"
      );

      const user = request.user;

      if (!user) {
        return (request.paymentInfo = null);
      }

      const paymentInfo = await subscriptionService.getUserSubscription(
        user.id
      );
      request.paymentInfo = paymentInfo;
    });
  },
  {
    name: "payment",
    dependencies: ["auth", "di"],
  }
);

declare module "fastify" {
  export interface FastifyRequest {
    paymentInfo: {
      firstPaidAt: Date;
      paidUntil: Date;
    } | null;
  }
}
