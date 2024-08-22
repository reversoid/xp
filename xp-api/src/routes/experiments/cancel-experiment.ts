import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { subscriptionGuard } from "../../utils/guards/subscription.guard.js";
import { NoActiveExperimentException } from "../../services/experiment/errors.js";

const cancelExperiment: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const experimentService = fastify.diContainer.resolve("experimentService");

  fastify.delete(
    "/",
    {
      preHandler: [authGuard, subscriptionGuard],
      schema: {},
    },
    async function (request, reply) {
      const user = request.user!;

      try {
        const experiment = await experimentService.cancelExperiment(user.id);

        return reply.send({ experiment });
      } catch (error) {
        if (error instanceof NoActiveExperimentException) {
          return reply.conflict("NO_ACTIVE_EXPERIMENT");
        }

        throw error;
      }
    }
  );
};

export default cancelExperiment;
