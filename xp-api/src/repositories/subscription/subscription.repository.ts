import { PrismaClient } from "@prisma/client";
import { User } from "../../models/user.js";
import { selectSubscription } from "../../models/subscription.js";

export class SubscriptionRepository {
  private readonly prismaClient: PrismaClient;

  constructor({ prismaClient }: { prismaClient: PrismaClient }) {
    this.prismaClient = prismaClient;
  }

  async linkUserToSubscription(
    userId: User["id"],
    tgUsername: User["tgUsername"]
  ): Promise<boolean> {
    return this.prismaClient.subscription
      .update({
        data: { userId },
        where: { tgUsername },
      })
      .then(() => true)
      .catch(() => false);
  }

  async getUserSubscription(userId: User["id"]) {
    const subscription = await this.prismaClient.subscription.findFirst({
      where: { userId },
      select: selectSubscription,
    });

    if (!subscription) {
      return null;
    }

    return subscription;
  }
}
