import fastifyPlugin from "fastify-plugin";

export default fastifyPlugin(async (fastify) => {
  fastify.setReplySerializer(function (payload, statusCode) {
    return JSON.stringify(payload, (key, value) =>
      typeof value === "bigint" ? value.toString() : value
    );
  });
});
