import { ApiProperty } from '@nestjs/swagger';

export class SwaggerPaginatedResponse {
  @ApiProperty({ nullable: true, type: String })
  next_key: string | null;
}

export interface ISwaggerPaginatedResponse<T> {
  items: T[];
}
