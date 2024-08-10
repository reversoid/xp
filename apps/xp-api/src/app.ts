import AutoLoad, { AutoloadPluginOptions } from "@fastify/autoload";
import { FastifyPluginAsync } from "fastify";
import * as path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export type AppOptions = {
  // Place your custom options for app below here.
} & Partial<AutoloadPluginOptions>;

// Pass --options via CLI arguments in command to enable these options.
const options: AppOptions = {};

const app: FastifyPluginAsync<AppOptions> = async (
  fastify,
  opts
): Promise<void> => {
  // Some code here

  fastify.setErrorHandler((error, _request, reply) => {
    if (error.statusCode === 400) {
      try {
        const errorsObjects = JSON.parse(error.message);
        return reply.code(400).send({
          message: "BAD_REQUEST",
          errors: errorsObjects,
        });
      } catch (error) {}
    }

    const isInternalError = error.statusCode === undefined;

    if (isInternalError) {
      console.error(error);

      return reply.code(500).send({ message: "INTERNAL_ERROR" });
    }

    const message = error.message.toLocaleUpperCase().split(" ").join("_");

    reply.code(error.statusCode ?? 500).send({ message });
  });

  // Do not touch the following lines

  // This loads all plugins defined in plugins
  // those should be support plugins that are reused
  // through your application
  void fastify.register(AutoLoad, {
    dir: path.join(__dirname, "plugins"),
    options: opts,
    forceESM: true,
  });

  // This loads all plugins defined in routes
  // define your routes in one of these
  void fastify.register(AutoLoad, {
    dir: path.join(__dirname, "routes"),
    options: opts,
    forceESM: true,
  });
};

export default app;
export { app, options };
