import fastifyPlugin from "fastify-plugin";

export default fastifyPlugin(
  async (fastify) => {
    fastify.addHook("preHandler", async (request, reply) => {
      const userService = fastify.diContainer.resolve("userService");

      const user = request.user;

      if (!user) {
        return (request.paymentInfo = null);
      }

      const paymentInfo = await userService.getUserPayment(user.id);
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
      lastPaidAt: Date;
      paidUntil: Date;
    } | null;
  }
}
