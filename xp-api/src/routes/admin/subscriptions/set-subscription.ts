import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { z } from "zod";

const setSubscriptionDto = z.object({
  username: z.string(),
  until: z.string().datetime(),
});

const setSubscription: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const subscriptionService = fastify.diContainer.resolve(
    "subscriptionService"
  );

  fastify.put(
    "/",
    {
      // TODO need admin auth handler?
      preHandler: [],
      schema: { body: setSubscriptionDto },
    },
    async function (request, reply) {
      const username = request.body.username;
      const until = new Date(request.body.until);

      const subscription = await subscriptionService.upsertSubscription(
        username,
        until
      );

      return reply.send({ subscription });
    }
  );
};

export default setSubscription;
