import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { subscriptionGuard } from "../../utils/guards/subscription.guard.js";
import { z } from "zod";

const getRandomObservations: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const observationService = fastify.diContainer.resolve("observationService");

  fastify.get(
    "/random",
    {
      preHandler: [authGuard, subscriptionGuard],
      schema: {
        querystring: z.object({
          limit: z.coerce.number().int().min(1).default(3),
        }),
      },
    },
    async function (request, reply) {
      const user = request.user!;

      const { limit } = request.query;

      const observations = await observationService.getRandomUnseenObservations(
        user.id,
        limit
      );

      return reply.send({ observations });
    }
  );
};

export default getRandomObservations;
