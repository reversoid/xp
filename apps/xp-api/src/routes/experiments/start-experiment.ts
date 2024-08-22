import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { subscriptionGuard } from "../../utils/guards/subscription.guard.js";
import { AlreadyStartedExperimentException } from "core-sdk/services/experiment/errors";

const getRandomObservations: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const experimentService = fastify.diContainer.resolve("experimentService");

  fastify.put(
    "/",
    {
      preHandler: [authGuard, subscriptionGuard],
      schema: {},
    },
    async function (request, reply) {
      const user = request.user!;

      try {
        const experiment = await experimentService.startExperiment(user.id);

        return reply.send({ experiment });
      } catch (error) {
        if (error instanceof AlreadyStartedExperimentException) {
          return reply.conflict("ALREADY_STARTED_EXPERIMENT");
        }

        throw error;
      }
    }
  );
};

export default getRandomObservations;
