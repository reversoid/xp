import { ApiProperty } from '@nestjs/swagger';
import { Transform } from 'class-transformer';
import { IsOptional } from 'class-validator';
import { DateTime } from 'luxon';
import { LimitQueryDTO } from './limit.query.dto';

export function ToDateTime() {
  return Transform(({ value }) => DateTime.fromISO(value), {
    toClassOnly: true,
  });
}

export class PaginationQueryDTO extends LimitQueryDTO {
  @ApiProperty({
    type: 'string',
    format: 'date-time',
    required: false,
    description: 'Lower bound date',
  })
  @IsOptional()
  @ToDateTime()
  lower_bound?: DateTime;
}
