import dayjs from "dayjs";
import { User } from "../../models/user.js";
import { SubscriptionRepository } from "../../repositories/subscription/subscription.repository.js";
import { TrialAlreadyTakenException } from "./errors.js";

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

  async checkAbilityToTakeTrial(userId: User["id"]) {
    const existingSubscription = await this.getUserSubscription(userId);

    if (existingSubscription) {
      throw new TrialAlreadyTakenException();
    }
  }

  async createTrialSubscription(
    userId: User["id"],
    tgUsername: User["tgUsername"]
  ) {
    await this.checkAbilityToTakeTrial(userId);

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
