import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { requestPaginationSchema } from "../../utils/pagination/schemas.js";
import { authGuard } from "../../utils/guards/auth.guard.js";

const getProfile: FastifyPluginAsyncZod = async (fastify): Promise<void> => {
  const experimentService = fastify.diContainer.resolve("experimentService");
  const observationService = fastify.diContainer.resolve("observationService");

  fastify.get(
    "/",
    { preHandler: [authGuard] },
    async function (request, reply) {
      const user = request.user!;
      return reply.send({ user });
    }
  );

  fastify.get(
    "/observations",
    { preHandler: [authGuard] },
    async function (request, reply) {
      const pagination = requestPaginationSchema.safeParse(request.query).data;

      const user = request.user!;

      const observations = await observationService.getUserObservations(
        user.id,
        {
          creationOrder: "desc",
          limit: pagination?.limit ?? 5,
          cursor: pagination?.cursor,
        }
      );

      return reply.send({ observations });
    }
  );

  fastify.get(
    "/experiments",
    { preHandler: [authGuard] },
    async function (request, reply) {
      const pagination = requestPaginationSchema.safeParse(request.query).data;

      const user = request.user!;

      const experiments = await experimentService.getUserExperiments(user.id, {
        creationOrder: "desc",
        limit: pagination?.limit ?? 5,
        cursor: pagination?.cursor,
      });

      return reply.send({ experiments });
    }
  );
};

export default getProfile;
