import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";

const getProfile: FastifyPluginAsyncZod = async (fastify): Promise<void> => {
  fastify.get(
    "/",

    async function (request, reply) {
      const user = request.user!;
      return reply.send({ user });
    }
  );
};

export default getProfile;
