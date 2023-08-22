import { DataSource, LessThanOrEqual } from 'typeorm';
import { Observation } from '../entities/observation.entity';
import { Injectable } from '@nestjs/common';
import { DateTime } from 'luxon';
import { PaginatedRepository } from 'src/shared/paginated.repository';
import { ObservationView } from '../entities/observation-view.entity';
import { User } from 'src/modules/user/entities/user.entity';

@Injectable()
export class ObservationRepository extends PaginatedRepository<Observation> {
  constructor(dataSource: DataSource) {
    super(Observation, dataSource.createEntityManager());
  }

  async getRandomObservations(amount: number, forUserId: number) {
    const query = super
      .createQueryBuilder('observation')
      .leftJoin(
        ObservationView,
        'observationView',
        'observation.id = observationView.observationId AND observationView.userId = :userId',
        { userId: forUserId },
      )
      .leftJoin(User, 'user', 'observation.userId = user.id', {
        userId: forUserId,
      })
      .select([
        'observation.id',
        'observation.text',
        'observation.tg_photo_id',
        'observation.tg_document_id',
        'observation.tg_voice_id',
        'observation.tg_video_id',
        'observation.tg_video_note_id',
        'observation.file_urls',
        'observation.tg_media_group',
        'observation.created_at',
      ])
      .addSelect('RANDOM()', 'random')
      .where('observationView.id IS NULL')
      .andWhere('user.id != :userId', { userId: forUserId })
      .orderBy('random')
      .take(amount);

    return query.getMany();
  }

  async getUserObservations(userId: number, limit = 10, lowerBound?: DateTime) {
    const observations = await this.find({
      where: {
        user: { id: userId },
        created_at: lowerBound && LessThanOrEqual(lowerBound),
      },
      order: { created_at: 'DESC' },
      take: limit + 1,
    });
    return this.processPaginationByCreatedDate(observations, limit);
  }
}
