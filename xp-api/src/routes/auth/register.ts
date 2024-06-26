import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { z } from "zod";
import { UserAlreadyExtistsException } from "../../services/auth/errors.js";

export const registerSchema = z.object({
  email: z.string().email(),
  username: z.string().min(1),
  password: z.string().min(8),
});

const register: FastifyPluginAsyncZod = async (fastify): Promise<void> => {
  const authService = fastify.diContainer.resolve("authService");
  const lucia = fastify.diContainer.resolve("lucia");

  fastify.post(
    "/register",
    {
      schema: { body: registerSchema },
    },
    async function (request, reply) {
      const { email, password, username } = request.body;

      try {
        const { sessionId } = await authService.register({
          email,
          password,
          username,
        });
        const cookie = lucia.createSessionCookie(sessionId);

        reply.setCookie(cookie.name, cookie.value, {
          ...cookie.attributes,
          signed: true,
        });

        return;
      } catch (error) {
        if (error instanceof UserAlreadyExtistsException) {
          return reply.conflict("USER_ALREADY_EXISTS");
        }
      }
    }
  );
};

export default register;
