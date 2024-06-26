import fp from "fastify-plugin";
import fastifyRedis from "@fastify/redis";

export type RedisClient = fastifyRedis.FastifyRedis;

export default fp(
  async (fastify) => {
    await fastify.register(fastifyRedis, {
      closeClient: true,
      port: fastify.config.REDIS_PORT,
      name: fastify.config.REDIS_NAME,
      password: fastify.config.REDIS_PASSWORD,
    });
  },
  { name: "redis", dependencies: ["env"] }
);
