import { DataSource, Repository } from 'typeorm';
import { Observation } from '../entities/observation.entity';
import { Injectable } from '@nestjs/common';

@Injectable()
export class ObservationRepository extends Repository<Observation> {
  constructor(dataSource: DataSource) {
    super(Observation, dataSource.createEntityManager());
  }

  async getRandomObservations(amount: number, userIdToIgnore?: number) {
    const query = super
      .createQueryBuilder('observation')
      .select('observation')
      .addSelect('RANDOM()', 'random')
      .leftJoin('observation.user', 'user')
      .orderBy('random')
      .take(amount);

    if (userIdToIgnore !== undefined) {
      query.where('user.id != :userIdToIgnore', { userIdToIgnore });
    }

    return query.getMany();
  }
}
