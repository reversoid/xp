import fp from "fastify-plugin";
import { z } from "zod";

const envSchema = z.object({
  PORT: z.coerce.number().int(),
  POSTGRES_URL: z.string(),
  MODE: z.enum(["prod", "stage", "dev"]),
  API_KEY: z.string(),
});

type Env = z.infer<typeof envSchema>;

declare module "fastify" {
  interface FastifyInstance {
    config: Env;
  }
}

export default fp(
  async (fastify) => {
    fastify.decorate("config", envSchema.parse(process.env));
  },
  { name: "env" }
);
