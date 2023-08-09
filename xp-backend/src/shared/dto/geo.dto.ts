import { IsDecimal, IsOptional } from 'class-validator';
import { Geo } from '../types/Geo.type';

export class GeoDTO implements Geo {
  @IsDecimal()
  longitude: number;

  @IsDecimal()
  latitude: string;

  @IsOptional()
  @IsDecimal()
  horizontal_accuracy?: number;
}
