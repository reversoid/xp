import fastifyPlugin from "fastify-plugin";
import { type Session, type User } from "lucia";
import { SESSION_COOKIE_NAME } from "./lucia.js";

export default fastifyPlugin(
  async (fastify) => {
    fastify.addHook("preHandler", async (request, reply) => {
      const lucia = fastify.lucia;

      const { value: sessionId, valid } = request.unsignCookie(
        request.cookies[SESSION_COOKIE_NAME] ?? ""
      );

      if (!valid || !sessionId) {
        request.user = null;
        request.session = null;
        return;
      }

      const { session, user } = await lucia.validateSession(sessionId);

      if (session && session.fresh) {
        const cookie = lucia.createSessionCookie(session.id);
        reply.setCookie(cookie.name, cookie.value, cookie.attributes);
      }

      if (!session) {
        const blankCookie = lucia.createBlankSessionCookie();
        reply.setCookie(
          blankCookie.name,
          blankCookie.value,
          blankCookie.attributes
        );
      }

      request.user = user;
      request.session = session;
    });
  },
  {
    name: "auth",
  }
);

declare module "fastify" {
  export interface FastifyRequest {
    user: User | null;
    session: Session | null;
  }
}
