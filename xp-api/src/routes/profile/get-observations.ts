import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { z } from "zod";

const getObservations: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const observationService = fastify.diContainer.resolve("observationService");

  fastify.get(
    "/observations",
    {
      preHandler: [authGuard],
      schema: {
        querystring: z.object({
          limit: z.coerce.number().int().min(1).default(5),
          cursor: z.string().nullish(),
        }),
      },
    },
    async function (request, reply) {
      const { limit, cursor } = request.query;

      const user = request.user!;

      const observations = await observationService.getUserObservations(
        user.id,
        {
          creationOrder: "desc",
          limit: limit,
          cursor: cursor ?? undefined,
        }
      );

      return reply.send({ observations });
    }
  );
};

export default getObservations;
