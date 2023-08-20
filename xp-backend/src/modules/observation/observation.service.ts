import { Injectable } from '@nestjs/common';
import { CreateObservationDTO } from './dto/create-observation.dto';
import { ObservationRepository } from './repositories/observation.repository';
import { Observation } from './entities/observation.entity';
import { ObservationViewRepository } from './repositories/observation-view.repository';

@Injectable()
export class ObservationService {
  constructor(
    private readonly observationRepository: ObservationRepository,
    private readonly observationViewRepository: ObservationViewRepository,
  ) {}

  async createObservation(
    dto: CreateObservationDTO,
    userId: number,
  ): Promise<Observation> {
    const newObservation = this.observationRepository.create({
      text: dto.text,
      tg_document_id: dto.document_id,
      tg_photo_id: dto.photo_id,
      tg_video_id: dto.video_id,
      tg_video_note_id: dto.video_note_id,
      tg_voice_id: dto.voice_id,
      tg_media_group: dto.media_group,
      user: {
        id: userId,
      },
    });

    const observation = await this.observationRepository.save(newObservation);
    return observation;
  }

  /** Get given amount of random observations.
   *
   * *If userId is specified, it will ignore user with this id*
   */
  async getRandomObservations(
    amount: number,
    userId: number,
  ): Promise<Observation[]> {
    return this.observationRepository.getRandomObservations(amount, userId);
  }

  async markObservationAsViewed(userId: number, observationId: number) {
    await this.observationViewRepository.markObservationAsViewed(
      userId,
      observationId,
    );
  }

  async markManyObservationsAsViewed(userId: number, observationIds: number[]) {
    await this.observationViewRepository.markManyObservationsAsViewed(
      userId,
      observationIds,
    );
  }
}
