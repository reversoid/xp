import { User } from "../../models/user.js";
import { SubscriptionRepository } from "../../repositories/subscription/subscription.repository.js";

export class SubscriptionService {
  private readonly subscriptionRepository: SubscriptionRepository;

  constructor({
    subscriptionRepository,
  }: {
    subscriptionRepository: SubscriptionRepository;
  }) {
    this.subscriptionRepository = subscriptionRepository;
  }

  async upsertSubscription(tgUsername: string, until: Date) {
    return this.subscriptionRepository.upsertSubscription(tgUsername, until);
  }

  async deleteSubscription(tgUsername: string) {
    return this.subscriptionRepository.deleteSubscription(tgUsername);
  }

  async getUserSubscription(userId: User["id"]) {
    return this.subscriptionRepository.getUserSubscription(userId);
  }

  async linkUserToSubscription(
    userId: User["id"],
    tgUsername: User["tgUsername"]
  ) {
    return this.subscriptionRepository.linkUserToSubscription(
      userId,
      tgUsername
    );
  }
}
