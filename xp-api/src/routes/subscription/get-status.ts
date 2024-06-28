import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";

enum SubscriptionStatuses {
  "ACTIVE" = "ACTIVE",
  "EXPIRED" = "EXPIRED",
  "NO_SUBSCRIPTION" = "NO_SUBSCRIPTION",
}

const getStatus: FastifyPluginAsyncZod = async (fastify): Promise<void> => {
  const subscriptionService = fastify.diContainer.resolve(
    "subscriptionService"
  );

  fastify.get(
    "/status",
    { preHandler: [authGuard] },
    async function (request, reply) {
      const user = request.user!;
      const existingSubscription =
        await subscriptionService.getUserSubscription(user.id);

      if (existingSubscription) {
        if (new Date() <= existingSubscription.paidUntil) {
          return reply.send({ status: SubscriptionStatuses.ACTIVE });
        }

        return reply.send({ status: SubscriptionStatuses.EXPIRED });
      }

      const subscriptionLinked =
        await subscriptionService.linkUserToSubscription(
          user.id,
          user.tgUsername
        );

      if (subscriptionLinked) {
        return reply.send({ status: SubscriptionStatuses.ACTIVE });
      }

      return reply.send({ status: SubscriptionStatuses.NO_SUBSCRIPTION });
    }
  );
};

export default getStatus;
