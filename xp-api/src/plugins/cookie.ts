import fastifyPlugin from "fastify-plugin";
import fastifyCookie from "@fastify/cookie";

export default fastifyPlugin(
  async (fastify) => {
    fastify.register(fastifyCookie, {
      hook: "onRequest",
      secret: fastify.config.COOKIE_SECRET,
    });
  },
  { dependencies: ["env"] }
);
