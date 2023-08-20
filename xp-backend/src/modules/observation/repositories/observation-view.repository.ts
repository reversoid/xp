import { Injectable } from '@nestjs/common';
import { DataSource, DeepPartial, Repository } from 'typeorm';
import { ObservationView } from '../entities/observation-view.entity';

@Injectable()
export class ObservationViewRepository extends Repository<ObservationView> {
  constructor(dataSource: DataSource) {
    super(ObservationView, dataSource.createEntityManager());
  }

  async markObservationAsViewed(userId: number, observationId: number) {
    return this.save({
      observation: { id: observationId },
      user: { id: userId },
    });
  }

  async markManyObservationsAsViewed(userId: number, observationIds: number[]) {
    await this.save(
      observationIds.map<DeepPartial<ObservationView>>((id) => ({
        user: { id: userId },
        observation: { id },
      })),
    );
  }

  async isObservationViewed(userId: number, observationId: number) {
    return this.findBy({
      observation: { id: observationId },
      user: { id: userId },
    });
  }
}
