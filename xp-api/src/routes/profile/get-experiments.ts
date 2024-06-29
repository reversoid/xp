import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { z } from "zod";

const getExperiments: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const experimentService = fastify.diContainer.resolve("experimentService");

  fastify.get(
    "/experiments",
    {
      preHandler: [authGuard],
      schema: {
        querystring: z.object({
          limit: z.number().int().min(1).default(5),
          cursor: z.string().nullish(),
        }),
      },
    },
    async function (request, reply) {
      const { limit, cursor } = request.query;

      const user = request.user!;

      const experiments = await experimentService.getUserExperiments(user.id, {
        creationOrder: "desc",
        limit: limit ?? 5,
        cursor: cursor ?? undefined,
      });

      return reply.send({ experiments });
    }
  );
};

export default getExperiments;
