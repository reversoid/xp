import { IsDecimal, IsOptional } from 'class-validator';

export class GeoDTO {
  @IsDecimal()
  longitude: number;

  @IsDecimal()
  latitude: string;

  @IsOptional()
  @IsDecimal()
  horizontal_accuracy?: number;
}
