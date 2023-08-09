import { DataSource, Repository } from 'typeorm';
import { Observation } from '../entities/observation.entity';
import { Injectable } from '@nestjs/common';

@Injectable()
export class ObservationRepository extends Repository<Observation> {
  constructor(dataSource: DataSource) {
    super(Observation, dataSource.createEntityManager());
  }

  async getRandomObservations(amount: number, userIdToIgnore?: number) {
    const randomObservations = await super
      .createQueryBuilder('observation')
      .leftJoin('observation.user', 'user')
      .where('user.id != :userIdToIgnore', { userIdToIgnore })
      .orderBy('RANDOM()')
      .take(amount)
      .getMany();

    return randomObservations;
  }
}
