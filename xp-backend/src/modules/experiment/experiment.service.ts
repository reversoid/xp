import { HttpException, Injectable } from '@nestjs/common';
import { DateTime } from 'luxon';
import { MoreThan } from 'typeorm';
import { FinishExperimentDTO } from './dto/finish-experiment.dto';
import { ExperimentStatus } from './entities/experiment.entity';
import { ExperimentRepository } from './repository/experiment.repository';

class AlreadyExistingExperimentException extends HttpException {
  constructor() {
    super('EXPERIMENT_ALREADY_STARTED', 423);
  }
}

class NotExistingExperimentException extends HttpException {
  constructor() {
    super('EXPERIMENT_NOT_STARTED', 423);
  }
}

@Injectable()
export class ExperimentService {
  constructor(private experimentRepository: ExperimentRepository) {}

  async runExperiment(userId: number, observationsIds: number[]) {
    await this.validateExistingExperiments(userId);

    const newExperiment = this.experimentRepository.create({
      status: ExperimentStatus.STARTED,
      complete_by: DateTime.now().plus({ hour: 24 }),
      user: { id: userId },
      observations: observationsIds.map((id) => ({ id })),
    });

    const experiment = await this.experimentRepository.save(newExperiment);

    return experiment;
  }

  async finishExperiment(userId: number, dto: FinishExperimentDTO) {
    const existingExperiment = await this.findValidStartedExperiment(userId);
    if (!existingExperiment) {
      throw new NotExistingExperimentException();
    }

    const finishedExperiment = await this.experimentRepository.save({
      ...existingExperiment,
      completed_at: DateTime.now(),
      status: ExperimentStatus.COMPLETED,
      text: dto.text,
      geo: dto.geo,
      tg_document_id: dto.document_id,
      tg_media_group: dto.media_group,
      tg_photo_id: dto.photo_id,
      tg_video_id: dto.video_id,
      tg_video_note_id: dto.video_note_id,
      tg_voice_id: dto.voice_id,
    });

    return finishedExperiment;
  }

  async cancelExperiment(userId: number) {
    const startedExperiment = await this.findAnyStartedExperiment(userId);
    if (!startedExperiment) {
      throw new NotExistingExperimentException();
    }

    const experiment = await this.experimentRepository.save({
      id: startedExperiment.id,
      status: ExperimentStatus.CANCELED,
    });

    return experiment;
  }

  async getCurrentExperiment(userId: number) {
    return this.findValidStartedExperiment(userId);
  }

  private async validateExistingExperiments(userId: number) {
    const experimentAlreadyStarted = await this.findValidStartedExperiment(
      userId,
    );

    if (experimentAlreadyStarted) {
      throw new AlreadyExistingExperimentException();
    }
  }

  private findValidStartedExperiment(userId: number) {
    return this.experimentRepository.findOne({
      where: {
        user: {
          id: userId,
        },
        status: ExperimentStatus.STARTED,
        complete_by: MoreThan(DateTime.now()),
      },
    });
  }

  private findAnyStartedExperiment(userId: number) {
    return this.experimentRepository.findOne({
      where: {
        user: {
          id: userId,
        },
        status: ExperimentStatus.STARTED,
      },
      relations: { observations: true },
    });
  }
}
