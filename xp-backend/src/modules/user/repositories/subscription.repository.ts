import { Injectable } from '@nestjs/common';
import { DataSource, LessThanOrEqual } from 'typeorm';

import { Subscription } from '../entities/Subscription.entity';
import { DateTime } from 'luxon';
import { PaginatedRepository } from 'src/shared/paginated.repository';

@Injectable()
export class SubscriptionRepository extends PaginatedRepository<Subscription> {
  constructor(dataSource: DataSource) {
    super(Subscription, dataSource.createEntityManager());
  }

  async isFollowedByUsername(whoFollowsId: number, username: string) {
    const subscription = await this.findOneBy({
      followed: { username },
      follower: { id: whoFollowsId },
    });

    return Boolean(subscription);
  }

  async isFollowedById(whoFollowsId: number, userId: number) {
    const subscription = await this.findBy({
      followed: { id: userId },
      follower: { id: whoFollowsId },
    });
    return Boolean(subscription);
  }

  async followByUsername(whoFollowsId: number, whoToFollowId: number) {
    return this.save({
      followed: { id: whoToFollowId },
      follower: { id: whoFollowsId },
    });
  }

  async unfollowByUsername(whoFollowsId: number, username: string) {
    const subscription = await this.findBy({
      followed: { username },
      follower: { id: whoFollowsId },
    });
    if (!subscription) {
      return;
    }
    await this.softRemove(subscription);
  }

  async unfollowById(whoFollowsId: number, userId: number) {
    const subscription = await this.findBy({
      followed: { id: userId },
      follower: { id: whoFollowsId },
    });
    if (!subscription) {
      return;
    }
    await this.softRemove(subscription);
  }

  async getFollowees(userId: number, limit: number, lowerBound?: DateTime) {
    const followees = await this.find({
      where: {
        follower: { id: userId },
        created_at: lowerBound && LessThanOrEqual(lowerBound),
      },
      relations: {
        followed: true,
      },
      take: limit + 1,
      order: {
        created_at: 'DESC',
      },
    });

    return this.processPaginationByCreatedDate(followees, limit);
  }
}
