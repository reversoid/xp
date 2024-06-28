import { Experiment } from "../../models/experiment.js";
import { User } from "../../models/user.js";
import { ExperimentRepository } from "../../repositories/experiment/experiment.repository.js";
import { PaginatedData } from "../../utils/pagination/paginated-data.js";
import {
  AlreadyStartedExperimentException,
  NoActiveExperimentException,
} from "./errors.js";
import { CompleteExperimentDto } from "./types.js";

export class ExperimentService {
  private readonly experimentRepository: ExperimentRepository;

  constructor({
    experimentRepository,
  }: {
    experimentRepository: ExperimentRepository;
  }) {
    this.experimentRepository = experimentRepository;
  }

  async getUserExperiments(
    userId: User["id"],
    options: { limit: number; creationOrder: "asc" | "desc"; cursor?: string }
  ): Promise<PaginatedData<Experiment>> {
    return this.experimentRepository.getUserExperiments(userId, {
      creationOrder: options.creationOrder,
      limit: options.limit,
      cursor: options.cursor,
    });
  }

  async startExperiment(userId: User["id"]): Promise<Experiment> {
    const activeExperiment =
      await this.experimentRepository.getUserActiveExperiment(userId);

    if (activeExperiment) {
      throw new AlreadyStartedExperimentException();
    }

    return this.experimentRepository.createEmptyExperiment(userId);
  }

  async completeExperiment(
    userId: User["id"],
    dto: CompleteExperimentDto
  ): Promise<Experiment> {
    const activeExperiment =
      await this.experimentRepository.getUserActiveExperiment(userId);

    if (!activeExperiment) {
      throw new NoActiveExperimentException();
    }

    await this.experimentRepository.fillExperiment(activeExperiment.id, {
      tgText: dto.tgText,
      tgDocumentId: dto.tgDocumentId,
      tgGeo: dto.tgGeo,
      tgMediaGroup: dto.tgMediaGroup,
      tgPhotoId: dto.tgPhotoId,
      tgVideoId: dto.tgVideoId,
      tgVideoNoteId: dto.tgVideoNoteId,
      tgVoiceId: dto.tgVoiceId,
    });

    return this.experimentRepository.markExperimentAsCompleted(
      activeExperiment.id
    );
  }

  async cancelExperiment(userId: User["id"]): Promise<Experiment> {
    const activeExperiment =
      await this.experimentRepository.getUserActiveExperiment(userId);

    if (!activeExperiment) {
      throw new NoActiveExperimentException();
    }

    return this.experimentRepository.markExperimentAsCanceled(
      activeExperiment.id
    );
  }
}
