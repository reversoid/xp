import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { subscriptionGuard } from "../../utils/guards/subscription.guard.js";

const completeExperiment: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const experimentService = fastify.diContainer.resolve("experimentService");

  fastify.get(
    "/",
    {
      preHandler: [authGuard, subscriptionGuard],
    },
    async function (request, reply) {
      const user = request.user!;

      const experiment = await experimentService.getUserActiveExperiment(
        user.id
      );

      return reply.send({ experiment });
    }
  );
};

export default completeExperiment;
