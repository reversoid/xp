import { fastifyPlugin } from "fastify-plugin";
import { verifyRequestOrigin } from "lucia";

export default fastifyPlugin(
  async (fastify) => {
    if (fastify.config.MODE !== "prod") {
      return;
    }

    fastify.addHook("preHandler", (request, reply, done) => {
      if (request.method === "GET") {
        return done();
      }

      const originHeader = request.headers.origin ?? null;
      // NOTE: You may need to use `X-Forwarded-Host` instead
      const hostHeader = request.headers.host ?? null;
      if (
        !originHeader ||
        !hostHeader ||
        !verifyRequestOrigin(originHeader, [hostHeader])
      ) {
        return reply.status(403);
      }
    });
  },
  {
    name: "csrf",
    dependencies: ["env"],
  }
);
