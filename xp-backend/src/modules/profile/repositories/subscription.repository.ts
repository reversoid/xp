import { Injectable } from '@nestjs/common';
import { DataSource, LessThanOrEqual } from 'typeorm';

import { Subscription } from '../entities/Subscription';
import { DateTime } from 'luxon';
import { PaginatedRepository } from 'src/shared/paginated.repository';

@Injectable()
export class SubscriptionRepository extends PaginatedRepository<Subscription> {
  constructor(dataSource: DataSource) {
    super(Subscription, dataSource.createEntityManager());
  }

  async isFollowedByUsername(whoFollowsId: number, username: string) {
    const subscription = await this.findBy({
      followee: { username },
      follower: { id: whoFollowsId },
    });
    return Boolean(subscription);
  }

  async followByUsername(whoFollowsId: number, username: string) {
    const subscription = this.create({
      followee: { username },
      follower: { id: whoFollowsId },
    });
    return this.save(subscription);
  }

  async unfollowByUsername(whoFollowsId: number, username: string) {
    const subscription = await this.findBy({
      followee: { username },
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
        followee: true,
      },
      take: limit + 1,
      order: {
        created_at: 'DESC',
      },
    });
    return this.processPaginationByCreatedDate(followees, limit);
  }
}
