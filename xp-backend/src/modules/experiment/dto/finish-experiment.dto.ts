import { Type } from 'class-transformer';
import { IsOptional, IsString, ValidateNested } from 'class-validator';
import { GeoDTO } from 'src/shared/dto/geo.dto';

export class FinishExperimentDTO {
  @IsString()
  text: string;

  @IsOptional()
  @IsString()
  photo_id: string;

  @IsOptional()
  @IsString()
  video_id: string;

  @IsOptional()
  @IsString()
  video_note_id: string;

  @IsOptional()
  @IsString()
  voice_id: string;

  @IsOptional()
  @IsString()
  document_id: string;

  @IsOptional()
  @IsString()
  media_group_id?: string;

  @IsOptional()
  @ValidateNested()
  @Type(() => GeoDTO)
  geo: GeoDTO;
}
