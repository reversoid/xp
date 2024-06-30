import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { z } from "zod";
import { UserAlreadyExistsException } from "../../services/auth/errors.js";

export const registerSchema = z.object({
  tgId: z.coerce.bigint(),
  tgUsername: z.string().max(32).min(3),
});

const register: FastifyPluginAsyncZod = async (fastify): Promise<void> => {
  const authService = fastify.diContainer.resolve("authService");

  fastify.post(
    "/register",
    {
      schema: { body: registerSchema },
    },
    async function (request, reply) {
      const { tgId, tgUsername } = request.body;

      try {
        const user = await authService.register(tgId, tgUsername);
        return reply.send({ user });
      } catch (error) {
        if (error instanceof UserAlreadyExistsException) {
          return reply.conflict("USER_ALREADY_EXISTS");
        }

        throw error;
      }
    }
  );
};

export default register;
