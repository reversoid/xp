import { IsOptional, IsString } from 'class-validator';

export class CreateObservationDTO {
  @IsOptional()
  @IsString()
  text?: string;

  @IsOptional()
  @IsString()
  photo_id?: string;

  @IsOptional()
  @IsString()
  document_id?: string;

  @IsOptional()
  @IsString()
  voice_id?: string;

  @IsOptional()
  @IsString()
  video_id?: string;

  @IsOptional()
  @IsString()
  video_note_id?: string;
}
