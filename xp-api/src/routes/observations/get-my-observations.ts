import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { z } from "zod";

const getMyObservations: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const observationService = fastify.diContainer.resolve("observationService");

  fastify.get(
    "/",
    {
      preHandler: [authGuard],
      schema: {
        querystring: z.object({
          limit: z.number().int().min(1).default(5),
          cursor: z.string().min(1).nullish(),
        }),
      },
    },
    async function (request, reply) {
      const user = request.user!;

      const { limit } = request.query;

      const observations = await observationService.getUserObservations(
        user.id,
        { limit, creationOrder: "desc" }
      );

      return reply.send({ observations });
    }
  );
};

export default getMyObservations;
