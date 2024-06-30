import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { TrialAlreadyTakenException } from "../../services/subscription/errors.js";

const startTrial: FastifyPluginAsyncZod = async (fastify): Promise<void> => {
  const subscriptionService = fastify.diContainer.resolve(
    "subscriptionService"
  );

  fastify.put(
    "/trial",
    { preHandler: [authGuard] },
    async function (request, reply) {
      const user = request.user!;

      try {
        const subscription = await subscriptionService.createTrialSubscription(
          user.id,
          user.tgUsername
        );

        return reply.send({ subscription });
      } catch (error) {
        if (error instanceof TrialAlreadyTakenException) {
          return reply.conflict("TRIAL_ALREADY_TAKEN");
        }

        throw error;
      }
    }
  );
};

export default startTrial;
