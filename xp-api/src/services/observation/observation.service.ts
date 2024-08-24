import { Observation } from "../../models/observation.js";
import { User } from "../../models/user.js";
import { ObservationRepository } from "../../repositories/observation/observation.repository.js";
import { PaginatedData } from "../../utils/pagination/paginated-data.js";
import { CreateObservationDto } from "./types.js";

export class ObservationService {
  observationRepository: ObservationRepository;

  constructor({
    observationRepository,
  }: {
    observationRepository: ObservationRepository;
  }) {
    this.observationRepository = observationRepository;
  }

  async getWaitingObservationsAmount() {
    return this.observationRepository.getWaitingObservationsAmount();
  }

  async createObservation(
    userId: User["id"],
    dto: CreateObservationDto
  ): Promise<Observation> {
    return this.observationRepository.createObservation(userId, {
      tgDocumentId: dto.tgDocumentId,
      tgPhotoId: dto.tgPhotoId,
      tgText: dto.tgText,
      tgVideoId: dto.tgVideoId,
      tgVideoNoteId: dto.tgVideoNoteId,
      tgVoiceId: dto.tgVoiceId,
      tgMediaGroup: dto.tgMediaGroup,
      tgGeo: dto.tgGeo,
    });
  }

  async markObservationAsSeen(
    userId: User["id"],
    observationId: Observation["id"]
  ) {
    await this.observationRepository.markObservationAsSeen(
      userId,
      observationId
    );
  }

  async getUserObservations(
    userId: User["id"],
    options: { limit: number; creationOrder: "asc" | "desc"; cursor?: string }
  ): Promise<PaginatedData<Observation>> {
    return this.observationRepository.getUserObservations(userId, {
      creationOrder: options.creationOrder,
      limit: options.limit,
      cursor: options.cursor,
    });
  }

  async getRandomUnseenObservations(
    userId: User["id"],
    limit: number
  ): Promise<Observation[]> {
    return this.observationRepository.getRandomUnseenObservations(
      userId,
      limit
    );
  }

  async approveObservation(
    observationId: Observation["id"]
  ): Promise<Observation> {
    return this.observationRepository.approveObservation(observationId);
  }

  async deleteObservation(observationId: Observation["id"]): Promise<void> {
    return this.observationRepository.deleteObservation(observationId);
  }

  async getWaitingObservations(
    limit: number,
    cursor?: string
  ): Promise<PaginatedData<Observation>> {
    return this.observationRepository.getWaitingObservations(limit, cursor);
  }
}
