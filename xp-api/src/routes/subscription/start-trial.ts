import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";

const startTrial: FastifyPluginAsyncZod = async (fastify): Promise<void> => {
  const subscriptionService = fastify.diContainer.resolve(
    "subscriptionService"
  );

  fastify.put(
    "/trial",
    { preHandler: [authGuard] },
    async function (request, reply) {
      const user = request.user!;

      const existingSubscription =
        await subscriptionService.getUserSubscription(user.id);

      if (existingSubscription) {
        return reply.conflict("HAVE_SUBSCRIPTION");
      }

      const subscription = await subscriptionService.createTrialSubscription(
        user.id,
        user.tgUsername
      );

      return reply.send({ subscription });
    }
  );
};

export default startTrial;
