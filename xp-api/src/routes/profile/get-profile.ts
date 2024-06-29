import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";

const getProfile: FastifyPluginAsyncZod = async (fastify): Promise<void> => {
  fastify.get(
    "/",
    { preHandler: [authGuard] },
    async function (request, reply) {
      const user = request.user!;
      return reply.send({ user });
    }
  );
};

export default getProfile;
