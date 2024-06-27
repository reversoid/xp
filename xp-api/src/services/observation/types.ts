export type CreateObservationDto = {
  tgText?: string;
  tgPhotoId?: string;
  tgVideoId?: string;
  tgVoiceId?: string;
  tgDocumentId?: string;
  tgVideoNoteId?: string;

  tgMediaGroup?: Array<{
    tgAudioId?: string;
    tgDocumentId?: string;
    tgPhotoId?: string;
    tgVideoId?: string;
  }>;

  tgGeo?: {
    longitude: number;
    latitude: number;
    horizontalAccuracy?: number;
  };
};
