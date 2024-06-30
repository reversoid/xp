import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { subscriptionGuard } from "../../utils/guards/subscription.guard.js";
import { z } from "zod";

const getRandomObservations: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const observationService = fastify.diContainer.resolve("observationService");

  fastify.put(
    "/:observationId/views",
    {
      preHandler: [authGuard, subscriptionGuard],
      schema: {
        params: z.object({ observationId: z.string().min(10).max(10) }),
      },
    },
    async function (request, reply) {
      const user = request.user!;

      const { observationId } = request.params;

      await observationService.markObservationAsSeen(user.id, observationId);

      return reply.send({});
    }
  );
};

export default getRandomObservations;
