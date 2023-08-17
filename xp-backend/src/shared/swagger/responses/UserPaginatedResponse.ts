import { ApiProperty } from '@nestjs/swagger';
import {
  ISwaggerPaginatedResponse,
  SwaggerPaginatedResponse,
} from './Paginated.response';
import { UserResponse } from './User.response';

export class UserPaginatedResponse
  extends SwaggerPaginatedResponse
  implements ISwaggerPaginatedResponse<UserResponse>
{
  @ApiProperty({ type: UserResponse, isArray: true })
  items: UserResponse[];
}
