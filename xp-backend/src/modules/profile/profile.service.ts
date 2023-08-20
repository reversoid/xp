import { BadRequestException, Injectable } from '@nestjs/common';
import { ObservationRepository } from '../observation/repositories/observation.repository';
import { ExperimentRepository } from '../experiment/repository/experiment.repository';
import { DateTime } from 'luxon';
import { SubscriptionRepository } from './repositories/subscription.repository';
import { PaginatedResponse } from 'src/shared/paginated.repository';
import { User } from '../user/entities/user.entity';
import { UserRepository } from '../user/repositories/user.repository';

class UserAlreadySubscribedException extends BadRequestException {
  constructor() {
    super('ALREADY_SUBSCRIBED');
  }
}

class UsernameTakenException extends BadRequestException {
  constructor() {
    super('USERNAME_TAKEN');
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
    private readonly userRepository: UserRepository,
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

  async unFollowUser(whoFollowsId: number, userId: number) {
    const isFollowed = await this.subscriptionRepository.isFollowedById(
      whoFollowsId,
      userId,
    );
    if (!isFollowed) {
      throw new UserUnSubscribedException();
    }
    return this.subscriptionRepository.unfollowById(whoFollowsId, userId);
  }

  async changeUsername(userId: number, username: string) {
    const user = await this.userRepository.getUserByUsername(username);

    if (user) {
      throw new UsernameTakenException();
    }

    return this.userRepository.editUsername(userId, username);
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
