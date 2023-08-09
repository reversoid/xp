import { Type } from 'class-transformer';
import { IsOptional, IsString, ValidateNested } from 'class-validator';
import { MediaGroupDTO } from 'src/shared/dto/media-group.dto';

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

  @IsOptional()
  @ValidateNested({ each: true })
  @Type(() => MediaGroupDTO)
  media_group: MediaGroupDTO[];
}
