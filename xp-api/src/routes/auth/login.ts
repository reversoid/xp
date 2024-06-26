import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { z } from "zod";
import {
  NoUserException,
  WrongCredentialsException,
} from "../../services/auth/errors.js";

export const loginSchema = z.object({
  email: z.string().email(),
  password: z.string(),
});

const login: FastifyPluginAsyncZod = async (fastify): Promise<void> => {
  const authService = fastify.diContainer.resolve("authService");
  const lucia = fastify.diContainer.resolve("lucia");

  fastify.post(
    "/login",
    { schema: { body: loginSchema } },
    async function (request, reply) {
      const { email, password } = request.body;

      try {
        const { sessionId } = await authService.login({ email, password });
        const cookie = lucia.createSessionCookie(sessionId);
        reply.setCookie(cookie.name, cookie.value, {
          ...cookie.attributes,
          signed: true,
        });
        return;
      } catch (error) {
        if (
          error instanceof WrongCredentialsException ||
          error instanceof NoUserException
        ) {
          return reply.badRequest("WRONG_CREDENTIALS");
        }
      }
    }
  );
};

export default login;
