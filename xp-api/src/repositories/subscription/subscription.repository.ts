import { PrismaClient } from "@prisma/client";
import { User } from "../../models/user.js";
import { selectSubscription, Subscription } from "../../models/subscription.js";

export class SubscriptionRepository {
  private readonly prismaClient: PrismaClient;

  constructor({ prismaClient }: { prismaClient: PrismaClient }) {
    this.prismaClient = prismaClient;
  }

  async upsertSubscription(
    tgUsername: string,
    until: Date
  ): Promise<Subscription> {
    return this.prismaClient.subscription.upsert({
      create: { tgUsername, until },
      update: { until },
      where: { tgUsername },

      select: selectSubscription,
    });
  }

  async deleteSubscription(tgUsername: string): Promise<void> {
    await this.prismaClient.subscription.delete({
      where: { tgUsername },
    });
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
