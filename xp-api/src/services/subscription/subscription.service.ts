import dayjs from "dayjs";
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

  async getUserSubscription(userId: User["id"]) {
    return this.subscriptionRepository.getUserSubscription(userId);
  }

  async createTrialSubscription(
    userId: User["id"],
    tgUsername: User["tgUsername"]
  ) {
    const until = dayjs().add(7, "days").toDate();

    return this.subscriptionRepository.createSubscription(
      userId,
      tgUsername,
      until
    );
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
