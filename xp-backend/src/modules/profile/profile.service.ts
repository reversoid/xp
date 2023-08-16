import { BadRequestException, Injectable } from '@nestjs/common';
import { ObservationRepository } from '../observation/repositories/observation.repository';
import { ExperimentRepository } from '../experiment/repository/experiment.repository';
import { DateTime } from 'luxon';
import { SubscriptionRepository } from './repositories/subscription.repository';
import { PaginatedResponse } from 'src/shared/paginated.repository';
import { User } from '../user/entities/user.entity';

class UserAlreadySubscribedException extends BadRequestException {
  constructor() {
    super('ALREADY_SUBSCRIBED');
  }
}

class UserUnSubscribedException extends BadRequestException {
  constructor() {
    super('ALREADY_UNSUBSCRIBED');
  }
}

@Injectable()
export class ProfileService {
  constructor(
    private readonly observationRepository: ObservationRepository,
    private readonly experimentRepository: ExperimentRepository,
    private readonly subscriptionRepository: SubscriptionRepository,
  ) {}

  async getUserObservations(
    userId: number,
    limit: number,
    lowerBound?: DateTime,
  ) {
    return this.observationRepository.getUserObservations(
      userId,
      limit,
      lowerBound,
    );
  }

  async getUserExperiments(
    userId: number,
    limit: number,
    lower_bound: DateTime,
  ) {
    return this.experimentRepository.getUserCompletedExperiments(
      userId,
      limit,
      lower_bound,
    );
  }

  async followUser(whoFollowsId: number, username: string) {
    const isFollowed = await this.subscriptionRepository.isFollowedByUsername(
      whoFollowsId,
      username,
    );
    if (isFollowed) {
      throw new UserAlreadySubscribedException();
    }
    return this.subscriptionRepository.followByUsername(whoFollowsId, username);
  }

  async unFollowUser(whoFollowsId: number, username: string) {
    const isFollowed = await this.subscriptionRepository.isFollowedByUsername(
      whoFollowsId,
      username,
    );
    if (!isFollowed) {
      throw new UserUnSubscribedException();
    }
    return this.subscriptionRepository.unfollowByUsername(
      whoFollowsId,
      username,
    );
  }

  async getUserFollowees(
    userId: number,
    limit: number,
    lowerBound?: DateTime,
  ): Promise<PaginatedResponse<User>> {
    const subscriptions = await this.subscriptionRepository.getFollowees(
      userId,
      limit,
      lowerBound,
    );
    return {
      ...subscriptions,
      items: subscriptions.items.map((s) => s.followee),
    };
  }
}
